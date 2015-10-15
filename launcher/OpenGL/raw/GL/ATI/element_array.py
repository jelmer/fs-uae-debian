'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ATI_element_array'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ATI_element_array',error_checker=_errors._error_checker)
GL_ELEMENT_ARRAY_ATI=_C('GL_ELEMENT_ARRAY_ATI',0x8768)
GL_ELEMENT_ARRAY_POINTER_ATI=_C('GL_ELEMENT_ARRAY_POINTER_ATI',0x876A)
GL_ELEMENT_ARRAY_TYPE_ATI=_C('GL_ELEMENT_ARRAY_TYPE_ATI',0x8769)
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei)
def glDrawElementArrayATI(mode,count):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei)
def glDrawRangeElementArrayATI(mode,start,end,count):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.c_void_p)
def glElementPointerATI(type,pointer):pass
# Calculate length of pointer from type:ElementPointerTypeATI