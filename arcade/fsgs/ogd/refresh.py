from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import time
from fsbc.Application import app
from fsbc.signal import Signal
from fsbc.task import Task
from fsgs.Database import Database
from fsgs.ogd.context import SynchronizerContext
from fsgs.ogd.lists import ListsSynchronizer
from fsgs.ogd.meta import MetaSynchronizer


class DatabaseRefreshTask(Task):

    def __init__(self):
        Task.__init__(self, "DatabaseRefreshTask")

    # def stop_check(self):
    #     pass

    def on_status(self, status):
        self.progressed(status)

    def run(self):
        with Database.get_instance() as database:
            self._run(database)

    def _run(self, database):
        # FIXME, dependency on fs_uae_launcher
        # from fs_uae_launcher.Scanner import Scanner
        # Scanner.start([], scan_for_files=False, update_game_database=True)
        from fs_uae_launcher.GameRatingSynchronizer import GameRatingSynchronizer
        from fs_uae_launcher.GameScanner import GameScanner

        context = SynchronizerContext()

        synchronizer = MetaSynchronizer(
            context, on_status=self.on_status, stop_check=self.stop_check)
        synchronizer.synchronize()

        synchronizer = GameRatingSynchronizer(
            context, database, on_status=self.on_status,
            stop_check=self.stop_check)
        synchronizer.username = "auth_token"
        synchronizer.password = app.settings["database_auth"]
        synchronizer.synchronize()

        synchronizer = ListsSynchronizer(
            context, on_status=self.on_status, stop_check=self.stop_check)
        synchronizer.synchronize()

        scanner = GameScanner(
            context, None, on_status=self.on_status,
            stop_check=self.stop_check)
        scanner.update_game_database(database)
        scanner.scan(database)

        # FIXME: review what signals should be sent when a scan is performed
        # FIXME: these should be removed soon
        app.settings["last_scan"] = str(time.time())
        app.settings["config_refresh"] = str(time.time())
        # this must be called from main, since callbacks are broadcast
        # when settings are changed
        Signal("scan_done").notify()
