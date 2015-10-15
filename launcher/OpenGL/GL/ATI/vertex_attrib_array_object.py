'''OpenGL extension ATI.vertex_attrib_array_object

This module customises the behaviour of the 
OpenGL.raw.GL.ATI.vertex_attrib_array_object to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension defines an interface that allows multiple sets of
	generic vertex attribute data to be cached in persistent server-side
	memory.  It is intended to allow client data to be stored in memory
	that can be directly accessed by graphics hardware.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ATI/vertex_attrib_array_object.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ATI.vertex_attrib_array_object import *
from OpenGL.raw.GL.ATI.vertex_attrib_array_object import _EXTENSION_NAME

def glInitVertexAttribArrayObjectATI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION