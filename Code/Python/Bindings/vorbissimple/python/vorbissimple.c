/* Generated by Pyrex 0.9.3 on Wed Jun 14 14:34:45 2006 */

#include "Python.h"
#include "structmember.h"
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#include "stdlib.h"
#include "vorbissimple.h"


typedef struct {PyObject **p; char *s;} __Pyx_InternTabEntry; /*proto*/
typedef struct {PyObject **p; char *s; long n;} __Pyx_StringTabEntry; /*proto*/
static PyObject *__Pyx_UnpackItem(PyObject *, int); /*proto*/
static int __Pyx_EndUnpack(PyObject *, int); /*proto*/
static int __Pyx_PrintItem(PyObject *); /*proto*/
static int __Pyx_PrintNewline(void); /*proto*/
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb); /*proto*/
static void __Pyx_ReRaise(void); /*proto*/
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list); /*proto*/
static PyObject *__Pyx_GetExcValue(void); /*proto*/
static int __Pyx_ArgTypeTest(PyObject *obj, PyTypeObject *type, int none_allowed, char *name); /*proto*/
static int __Pyx_TypeTest(PyObject *obj, PyTypeObject *type); /*proto*/
static int __Pyx_GetStarArgs(PyObject **args, PyObject **kwds, char *kwd_list[], int nargs, PyObject **args2, PyObject **kwds2); /*proto*/
static void __Pyx_WriteUnraisable(char *name); /*proto*/
static void __Pyx_AddTraceback(char *funcname); /*proto*/
static PyTypeObject *__Pyx_ImportType(char *module_name, char *class_name, long size);  /*proto*/
static int __Pyx_SetVtable(PyObject *dict, void *vtable); /*proto*/
static int __Pyx_GetVtable(PyObject *dict, void *vtabptr); /*proto*/
static PyObject *__Pyx_CreateClass(PyObject *bases, PyObject *dict, PyObject *name, char *modname); /*proto*/
static int __Pyx_InternStrings(__Pyx_InternTabEntry *t); /*proto*/
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t); /*proto*/
static PyObject *__Pyx_GetName(PyObject *dict, PyObject *name); /*proto*/

static PyObject *__pyx_m;
static PyObject *__pyx_b;
static int __pyx_lineno;
static char *__pyx_filename;
staticforward char **__pyx_f;

/* Declarations from vorbissimple */

staticforward PyTypeObject __pyx_type_12vorbissimple_vorbissimple;

struct __pyx_obj_12vorbissimple_vorbissimple {
  PyObject_HEAD
  ogg_vorbis_context (*oggVorbisContext);
  source_buffer (*sourceBuffer);
  decode_buffer (*decodeBuffer);
  PyObject *sourceQueue;
  long sourceQueueLen;
};

static PyTypeObject *__pyx_ptype_12vorbissimple_vorbissimple = 0;

/* Implementation of vorbissimple */

static int __pyx_f_12vorbissimple_12vorbissimple___new__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static int __pyx_f_12vorbissimple_12vorbissimple___new__(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  int __pyx_r;
  PyObject *__pyx_1 = 0;
  static char *__pyx_argnames[] = {0};
  if (!PyArg_ParseTupleAndKeywords(__pyx_args, __pyx_kwds, "", __pyx_argnames)) return -1;
  Py_INCREF(__pyx_v_self);

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":49 */
  ((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceBuffer = newSourceBuffer(0,BUFSIZE);

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":50 */
  ((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->oggVorbisContext = newOggVorbisContext();

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":51 */
  ((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->decodeBuffer = 0;

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":52 */
  __pyx_1 = PyList_New(0); if (!__pyx_1) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 52; goto __pyx_L1;}
  Py_DECREF(((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceQueue);
  ((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceQueue = __pyx_1;
  __pyx_1 = 0;

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":53 */
  ((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceQueueLen = 0;

  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1:;
  Py_XDECREF(__pyx_1);
  __Pyx_AddTraceback("vorbissimple.vorbissimple.__new__");
  __pyx_r = -1;
  __pyx_L0:;
  Py_DECREF(__pyx_v_self);
  return __pyx_r;
}

static void __pyx_f_12vorbissimple_12vorbissimple___dealloc__(PyObject *__pyx_v_self); /*proto*/
static void __pyx_f_12vorbissimple_12vorbissimple___dealloc__(PyObject *__pyx_v_self) {
  int __pyx_1;
  Py_INCREF(__pyx_v_self);

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":56 */
  __pyx_1 = (((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->decodeBuffer != 0);
  if (__pyx_1) {

    /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":57 */
    free(((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->decodeBuffer);

    /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":58 */
    ((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->decodeBuffer = 0;
    goto __pyx_L2;
  }
  __pyx_L2:;

  goto __pyx_L0;
  __pyx_L1:;
  __Pyx_AddTraceback("vorbissimple.vorbissimple.__dealloc__");
  __pyx_L0:;
  Py_DECREF(__pyx_v_self);
}

static PyObject *__pyx_n_append;
static PyObject *__pyx_n_len;

static PyObject *__pyx_f_12vorbissimple_12vorbissimple_sendBytesForDecode(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyObject *__pyx_f_12vorbissimple_12vorbissimple_sendBytesForDecode(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_bytes = 0;
  PyObject *__pyx_r;
  PyObject *__pyx_1 = 0;
  PyObject *__pyx_2 = 0;
  PyObject *__pyx_3 = 0;
  PyObject *__pyx_4 = 0;
  long __pyx_5;
  static char *__pyx_argnames[] = {"bytes",0};
  if (!PyArg_ParseTupleAndKeywords(__pyx_args, __pyx_kwds, "O", __pyx_argnames, &__pyx_v_bytes)) return 0;
  Py_INCREF(__pyx_v_self);
  Py_INCREF(__pyx_v_bytes);

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":61 */
  __pyx_1 = PyObject_GetAttr(((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceQueue, __pyx_n_append); if (!__pyx_1) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 61; goto __pyx_L1;}
  __pyx_2 = PyTuple_New(1); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 61; goto __pyx_L1;}
  Py_INCREF(__pyx_v_bytes);
  PyTuple_SET_ITEM(__pyx_2, 0, __pyx_v_bytes);
  __pyx_3 = PyObject_CallObject(__pyx_1, __pyx_2); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 61; goto __pyx_L1;}
  Py_DECREF(__pyx_1); __pyx_1 = 0;
  Py_DECREF(__pyx_2); __pyx_2 = 0;
  Py_DECREF(__pyx_3); __pyx_3 = 0;

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":62 */
  __pyx_1 = PyInt_FromLong(((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceQueueLen); if (!__pyx_1) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 62; goto __pyx_L1;}
  __pyx_2 = __Pyx_GetName(__pyx_b, __pyx_n_len); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 62; goto __pyx_L1;}
  __pyx_3 = PyTuple_New(1); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 62; goto __pyx_L1;}
  Py_INCREF(__pyx_v_bytes);
  PyTuple_SET_ITEM(__pyx_3, 0, __pyx_v_bytes);
  __pyx_4 = PyObject_CallObject(__pyx_2, __pyx_3); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 62; goto __pyx_L1;}
  Py_DECREF(__pyx_2); __pyx_2 = 0;
  Py_DECREF(__pyx_3); __pyx_3 = 0;
  __pyx_2 = PyNumber_Add(__pyx_1, __pyx_4); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 62; goto __pyx_L1;}
  Py_DECREF(__pyx_1); __pyx_1 = 0;
  Py_DECREF(__pyx_4); __pyx_4 = 0;
  __pyx_5 = PyInt_AsLong(__pyx_2); if (PyErr_Occurred()) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 62; goto __pyx_L1;}
  Py_DECREF(__pyx_2); __pyx_2 = 0;
  ((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceQueueLen = __pyx_5;

  __pyx_r = Py_None; Py_INCREF(__pyx_r);
  goto __pyx_L0;
  __pyx_L1:;
  Py_XDECREF(__pyx_1);
  Py_XDECREF(__pyx_2);
  Py_XDECREF(__pyx_3);
  Py_XDECREF(__pyx_4);
  __Pyx_AddTraceback("vorbissimple.vorbissimple.sendBytesForDecode");
  __pyx_r = 0;
  __pyx_L0:;
  Py_DECREF(__pyx_v_self);
  Py_DECREF(__pyx_v_bytes);
  return __pyx_r;
}

static PyObject *__pyx_n_NEEDDATA;
static PyObject *__pyx_n_min;
static PyObject *__pyx_n_ord;


static PyObject *__pyx_f_12vorbissimple_12vorbissimple___dequeueToDecoder(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyObject *__pyx_f_12vorbissimple_12vorbissimple___dequeueToDecoder(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  int __pyx_v_count;
  int __pyx_v_i;
  int __pyx_v_j;
  PyObject *__pyx_v_fragment;
  PyObject *__pyx_r;
  int __pyx_1;
  PyObject *__pyx_2 = 0;
  PyObject *__pyx_3 = 0;
  PyObject *__pyx_4 = 0;
  PyObject *__pyx_5 = 0;
  long __pyx_6;
  char __pyx_7;
  static char *__pyx_argnames[] = {0};
  if (!PyArg_ParseTupleAndKeywords(__pyx_args, __pyx_kwds, "", __pyx_argnames)) return 0;
  Py_INCREF(__pyx_v_self);
  __pyx_v_fragment = Py_None; Py_INCREF(__pyx_v_fragment);

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":72 */
  __pyx_1 = (((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceQueueLen < 58);
  if (__pyx_1) {

    /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":73 */
    __Pyx_Raise(__pyx_n_NEEDDATA, 0, 0);
    {__pyx_filename = __pyx_f[0]; __pyx_lineno = 73; goto __pyx_L1;}
    goto __pyx_L2;
  }
  __pyx_L2:;

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":76 */
  __pyx_2 = __Pyx_GetName(__pyx_b, __pyx_n_min); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 76; goto __pyx_L1;}
  __pyx_3 = PyInt_FromLong(((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceQueueLen); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 76; goto __pyx_L1;}
  __pyx_4 = PyInt_FromLong(BUFSIZE); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 76; goto __pyx_L1;}
  __pyx_5 = PyTuple_New(2); if (!__pyx_5) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 76; goto __pyx_L1;}
  PyTuple_SET_ITEM(__pyx_5, 0, __pyx_3);
  PyTuple_SET_ITEM(__pyx_5, 1, __pyx_4);
  __pyx_3 = 0;
  __pyx_4 = 0;
  __pyx_3 = PyObject_CallObject(__pyx_2, __pyx_5); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 76; goto __pyx_L1;}
  Py_DECREF(__pyx_2); __pyx_2 = 0;
  Py_DECREF(__pyx_5); __pyx_5 = 0;
  __pyx_1 = PyInt_AsLong(__pyx_3); if (PyErr_Occurred()) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 76; goto __pyx_L1;}
  Py_DECREF(__pyx_3); __pyx_3 = 0;
  __pyx_v_count = __pyx_1;

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":79 */
  __pyx_1 = (__pyx_v_count < BUFSIZE);
  if (__pyx_1) {
    __pyx_1 = (__pyx_v_count > (BUFSIZE - 58));
  }
  if (__pyx_1) {

    /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":80 */
    __pyx_v_count = (BUFSIZE - 58);
    goto __pyx_L3;
  }
  __pyx_L3:;

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":83 */
  ((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceBuffer->bytes = __pyx_v_count;

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":84 */
  ((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceQueueLen = (((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceQueueLen - __pyx_v_count);

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":85 */
  __pyx_v_i = 0;

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":86 */
  while (1) {
    __pyx_L4:;
    __pyx_1 = (__pyx_v_count > 0);
    if (!__pyx_1) break;

    /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":87 */
    __pyx_4 = PyInt_FromLong(0); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 87; goto __pyx_L1;}
    __pyx_2 = PyObject_GetItem(((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceQueue, __pyx_4); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 87; goto __pyx_L1;}
    Py_DECREF(__pyx_4); __pyx_4 = 0;
    Py_DECREF(__pyx_v_fragment);
    __pyx_v_fragment = __pyx_2;
    __pyx_2 = 0;

    /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":90 */
    __pyx_5 = __Pyx_GetName(__pyx_b, __pyx_n_min); if (!__pyx_5) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 90; goto __pyx_L1;}
    __pyx_3 = __Pyx_GetName(__pyx_b, __pyx_n_len); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 90; goto __pyx_L1;}
    __pyx_4 = PyTuple_New(1); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 90; goto __pyx_L1;}
    Py_INCREF(__pyx_v_fragment);
    PyTuple_SET_ITEM(__pyx_4, 0, __pyx_v_fragment);
    __pyx_2 = PyObject_CallObject(__pyx_3, __pyx_4); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 90; goto __pyx_L1;}
    Py_DECREF(__pyx_3); __pyx_3 = 0;
    Py_DECREF(__pyx_4); __pyx_4 = 0;
    __pyx_3 = PyInt_FromLong(__pyx_v_count); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 90; goto __pyx_L1;}
    __pyx_4 = PyTuple_New(2); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 90; goto __pyx_L1;}
    PyTuple_SET_ITEM(__pyx_4, 0, __pyx_2);
    PyTuple_SET_ITEM(__pyx_4, 1, __pyx_3);
    __pyx_2 = 0;
    __pyx_3 = 0;
    __pyx_2 = PyObject_CallObject(__pyx_5, __pyx_4); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 90; goto __pyx_L1;}
    Py_DECREF(__pyx_5); __pyx_5 = 0;
    Py_DECREF(__pyx_4); __pyx_4 = 0;
    __pyx_6 = PyInt_AsLong(__pyx_2); if (PyErr_Occurred()) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 90; goto __pyx_L1;}
    Py_DECREF(__pyx_2); __pyx_2 = 0;
    for (__pyx_v_j = 0; __pyx_v_j < __pyx_6; ++__pyx_v_j) {

      /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":91 */
      __pyx_3 = __Pyx_GetName(__pyx_b, __pyx_n_ord); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 91; goto __pyx_L1;}
      __pyx_5 = PyInt_FromLong(__pyx_v_j); if (!__pyx_5) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 91; goto __pyx_L1;}
      __pyx_4 = PyObject_GetItem(__pyx_v_fragment, __pyx_5); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 91; goto __pyx_L1;}
      Py_DECREF(__pyx_5); __pyx_5 = 0;
      __pyx_2 = PyTuple_New(1); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 91; goto __pyx_L1;}
      PyTuple_SET_ITEM(__pyx_2, 0, __pyx_4);
      __pyx_4 = 0;
      __pyx_5 = PyObject_CallObject(__pyx_3, __pyx_2); if (!__pyx_5) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 91; goto __pyx_L1;}
      Py_DECREF(__pyx_3); __pyx_3 = 0;
      Py_DECREF(__pyx_2); __pyx_2 = 0;
      __pyx_7 = PyInt_AsLong(__pyx_5); if (PyErr_Occurred()) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 91; goto __pyx_L1;}
      Py_DECREF(__pyx_5); __pyx_5 = 0;
      (((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceBuffer->buffer[__pyx_v_i]) = __pyx_7;

      /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":92 */
      __pyx_v_i = (__pyx_v_i + 1);
      __pyx_L6:;
    }
    __pyx_L7:;

    /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":94 */
    __pyx_v_count = (__pyx_v_count - __pyx_v_j);

    /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":97 */
    __pyx_4 = PyInt_FromLong(__pyx_v_j); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 97; goto __pyx_L1;}
    __pyx_3 = __Pyx_GetName(__pyx_b, __pyx_n_len); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 97; goto __pyx_L1;}
    __pyx_2 = PyTuple_New(1); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 97; goto __pyx_L1;}
    Py_INCREF(__pyx_v_fragment);
    PyTuple_SET_ITEM(__pyx_2, 0, __pyx_v_fragment);
    __pyx_5 = PyObject_CallObject(__pyx_3, __pyx_2); if (!__pyx_5) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 97; goto __pyx_L1;}
    Py_DECREF(__pyx_3); __pyx_3 = 0;
    Py_DECREF(__pyx_2); __pyx_2 = 0;
    if (PyObject_Cmp(__pyx_4, __pyx_5, &__pyx_1) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 97; goto __pyx_L1;}
    __pyx_1 = __pyx_1 == 0;
    Py_DECREF(__pyx_4); __pyx_4 = 0;
    Py_DECREF(__pyx_5); __pyx_5 = 0;
    if (__pyx_1) {

      /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":98 */
      __pyx_3 = PyInt_FromLong(0); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 98; goto __pyx_L1;}
      if (PyObject_DelItem(((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceQueue, __pyx_3) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 98; goto __pyx_L1;}
      Py_DECREF(__pyx_3); __pyx_3 = 0;
      goto __pyx_L8;
    }
    /*else*/ {

      /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":100 */
      __pyx_2 = PyInt_FromLong(0); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 100; goto __pyx_L1;}
      __pyx_4 = PyObject_GetItem(((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceQueue, __pyx_2); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 100; goto __pyx_L1;}
      Py_DECREF(__pyx_2); __pyx_2 = 0;
      __pyx_5 = PySequence_GetSlice(__pyx_4, __pyx_v_j, 0x7fffffff); if (!__pyx_5) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 100; goto __pyx_L1;}
      Py_DECREF(__pyx_4); __pyx_4 = 0;
      __pyx_2 = PyInt_FromLong(0); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 100; goto __pyx_L1;}
      if (PyObject_SetItem(((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceQueue, __pyx_2, __pyx_5) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 100; goto __pyx_L1;}
      Py_DECREF(__pyx_2); __pyx_2 = 0;
      Py_DECREF(__pyx_5); __pyx_5 = 0;
    }
    __pyx_L8:;
  }
  __pyx_L5:;

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":102 */
  sendBytesForDecode(((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->oggVorbisContext,((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->sourceBuffer);

  __pyx_r = Py_None; Py_INCREF(__pyx_r);
  goto __pyx_L0;
  __pyx_L1:;
  Py_XDECREF(__pyx_2);
  Py_XDECREF(__pyx_3);
  Py_XDECREF(__pyx_4);
  Py_XDECREF(__pyx_5);
  __Pyx_AddTraceback("vorbissimple.vorbissimple.__dequeueToDecoder");
  __pyx_r = 0;
  __pyx_L0:;
  Py_DECREF(__pyx_v_fragment);
  Py_DECREF(__pyx_v_self);
  return __pyx_r;
}

static PyObject *__pyx_n___dequeueToDecoder;
static PyObject *__pyx_n_RETRY;
static PyObject *__pyx_n_ERROR;

static PyObject *__pyx_k2p;

static char (__pyx_k2[]) = "";

static PyObject *__pyx_f_12vorbissimple_12vorbissimple__getAudio(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyObject *__pyx_f_12vorbissimple_12vorbissimple__getAudio(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_r;
  long __pyx_1;
  int __pyx_2;
  PyObject *__pyx_3 = 0;
  PyObject *__pyx_4 = 0;
  PyObject *__pyx_5 = 0;
  static char *__pyx_argnames[] = {0};
  if (!PyArg_ParseTupleAndKeywords(__pyx_args, __pyx_kwds, "", __pyx_argnames)) return 0;
  Py_INCREF(__pyx_v_self);

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":108 */
  while (1) {
    __pyx_L2:;
    __pyx_1 = 1;
    if (!__pyx_1) break;

    /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":109 */
    __pyx_2 = (((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->decodeBuffer != 0);
    if (__pyx_2) {

      /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":110 */
      free(((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->decodeBuffer);

      /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":111 */
      ((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->decodeBuffer = 0;
      goto __pyx_L4;
    }
    __pyx_L4:;

    /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":113 */
    ((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->decodeBuffer = getAudio(((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->oggVorbisContext);

    /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":115 */
    __pyx_2 = (((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->decodeBuffer->status == NEEDDATA);
    if (__pyx_2) {

      /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":116 */
      __pyx_3 = PyObject_GetAttr(__pyx_v_self, __pyx_n___dequeueToDecoder); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 116; goto __pyx_L1;}
      __pyx_4 = PyTuple_New(0); if (!__pyx_4) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 116; goto __pyx_L1;}
      __pyx_5 = PyObject_CallObject(__pyx_3, __pyx_4); if (!__pyx_5) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 116; goto __pyx_L1;}
      Py_DECREF(__pyx_3); __pyx_3 = 0;
      Py_DECREF(__pyx_4); __pyx_4 = 0;
      Py_DECREF(__pyx_5); __pyx_5 = 0;
      goto __pyx_L5;
    }
    /*else*/ {

      /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":118 */
      goto __pyx_L3;
    }
    __pyx_L5:;
  }
  __pyx_L3:;

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":121 */
  __pyx_2 = (((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->decodeBuffer->status == HAVEDATA);
  if (__pyx_2) {

    /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":123 */
    __pyx_2 = (((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->decodeBuffer->len > 0);
    if (__pyx_2) {

      /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":124 */
      __pyx_3 = PyString_FromStringAndSize(((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->decodeBuffer->buffer,((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->decodeBuffer->len); if (!__pyx_3) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 124; goto __pyx_L1;}
      __pyx_r = __pyx_3;
      __pyx_3 = 0;
      goto __pyx_L0;
      goto __pyx_L7;
    }
    /*else*/ {

      /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":126 */
      Py_INCREF(__pyx_k2p);
      __pyx_r = __pyx_k2p;
      goto __pyx_L0;
    }
    __pyx_L7:;
    goto __pyx_L6;
  }
  __pyx_L6:;

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":128 */
  __pyx_2 = (((struct __pyx_obj_12vorbissimple_vorbissimple *)__pyx_v_self)->decodeBuffer->status == NORMAL);
  if (__pyx_2) {

    /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":129 */
    __Pyx_Raise(__pyx_n_RETRY, 0, 0);
    {__pyx_filename = __pyx_f[0]; __pyx_lineno = 129; goto __pyx_L1;}
    goto __pyx_L8;
  }
  __pyx_L8:;

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":131 */
  __Pyx_Raise(__pyx_n_ERROR, 0, 0);
  {__pyx_filename = __pyx_f[0]; __pyx_lineno = 131; goto __pyx_L1;}

  __pyx_r = Py_None; Py_INCREF(__pyx_r);
  goto __pyx_L0;
  __pyx_L1:;
  Py_XDECREF(__pyx_3);
  Py_XDECREF(__pyx_4);
  Py_XDECREF(__pyx_5);
  __Pyx_AddTraceback("vorbissimple.vorbissimple._getAudio");
  __pyx_r = 0;
  __pyx_L0:;
  Py_DECREF(__pyx_v_self);
  return __pyx_r;
}

static PyObject *__pyx_k5p;

static char (__pyx_k5[]) = "Failed! :-)";

static PyObject *__pyx_f_12vorbissimple_12vorbissimple_fails(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyObject *__pyx_f_12vorbissimple_12vorbissimple_fails(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_r;
  static char *__pyx_argnames[] = {0};
  if (!PyArg_ParseTupleAndKeywords(__pyx_args, __pyx_kwds, "", __pyx_argnames)) return 0;
  Py_INCREF(__pyx_v_self);

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":135 */
  __Pyx_Raise(__pyx_k5p, 0, 0);
  {__pyx_filename = __pyx_f[0]; __pyx_lineno = 135; goto __pyx_L1;}

  __pyx_r = Py_None; Py_INCREF(__pyx_r);
  goto __pyx_L0;
  __pyx_L1:;
  __Pyx_AddTraceback("vorbissimple.vorbissimple.fails");
  __pyx_r = 0;
  __pyx_L0:;
  Py_DECREF(__pyx_v_self);
  return __pyx_r;
}

static __Pyx_InternTabEntry __pyx_intern_tab[] = {
  {&__pyx_n_ERROR, "ERROR"},
  {&__pyx_n_NEEDDATA, "NEEDDATA"},
  {&__pyx_n_RETRY, "RETRY"},
  {&__pyx_n___dequeueToDecoder, "__dequeueToDecoder"},
  {&__pyx_n_append, "append"},
  {&__pyx_n_len, "len"},
  {&__pyx_n_min, "min"},
  {&__pyx_n_ord, "ord"},
  {0, 0}
};

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_k2p, __pyx_k2, sizeof(__pyx_k2)},
  {&__pyx_k5p, __pyx_k5, sizeof(__pyx_k5)},
  {0, 0, 0}
};

static PyObject *__pyx_tp_new_12vorbissimple_vorbissimple(PyTypeObject *t, PyObject *a, PyObject *k) {
  PyObject *o = (*t->tp_alloc)(t, 0);
  struct __pyx_obj_12vorbissimple_vorbissimple *p = (struct __pyx_obj_12vorbissimple_vorbissimple *)o;
  p->sourceQueue = Py_None; Py_INCREF(p->sourceQueue);
  if (__pyx_f_12vorbissimple_12vorbissimple___new__(o, a, k) < 0) {
    Py_DECREF(o); o = 0;
  }
  return o;
}

static void __pyx_tp_dealloc_12vorbissimple_vorbissimple(PyObject *o) {
  struct __pyx_obj_12vorbissimple_vorbissimple *p = (struct __pyx_obj_12vorbissimple_vorbissimple *)o;
  {
    PyObject *etype, *eval, *etb;
    PyErr_Fetch(&etype, &eval, &etb);
    ++o->ob_refcnt;
    __pyx_f_12vorbissimple_12vorbissimple___dealloc__(o);
    if (PyErr_Occurred()) PyErr_WriteUnraisable(o);
    --o->ob_refcnt;
    PyErr_Restore(etype, eval, etb);
  }
  Py_XDECREF(p->sourceQueue);
  (*o->ob_type->tp_free)(o);
}

static int __pyx_tp_traverse_12vorbissimple_vorbissimple(PyObject *o, visitproc v, void *a) {
  int e;
  struct __pyx_obj_12vorbissimple_vorbissimple *p = (struct __pyx_obj_12vorbissimple_vorbissimple *)o;
  if (p->sourceQueue) {
    e = (*v)(p->sourceQueue, a); if (e) return e;
  }
  return 0;
}

static int __pyx_tp_clear_12vorbissimple_vorbissimple(PyObject *o) {
  struct __pyx_obj_12vorbissimple_vorbissimple *p = (struct __pyx_obj_12vorbissimple_vorbissimple *)o;
  Py_XDECREF(p->sourceQueue);
  p->sourceQueue = Py_None; Py_INCREF(p->sourceQueue);
  return 0;
}

static struct PyMethodDef __pyx_methods_12vorbissimple_vorbissimple[] = {
  {"sendBytesForDecode", (PyCFunction)__pyx_f_12vorbissimple_12vorbissimple_sendBytesForDecode, METH_VARARGS|METH_KEYWORDS, 0},
  {"__dequeueToDecoder", (PyCFunction)__pyx_f_12vorbissimple_12vorbissimple___dequeueToDecoder, METH_VARARGS|METH_KEYWORDS, 0},
  {"_getAudio", (PyCFunction)__pyx_f_12vorbissimple_12vorbissimple__getAudio, METH_VARARGS|METH_KEYWORDS, 0},
  {"fails", (PyCFunction)__pyx_f_12vorbissimple_12vorbissimple_fails, METH_VARARGS|METH_KEYWORDS, 0},
  {0, 0, 0, 0}
};

static PyNumberMethods __pyx_tp_as_number_vorbissimple = {
  0, /*nb_add*/
  0, /*nb_subtract*/
  0, /*nb_multiply*/
  0, /*nb_divide*/
  0, /*nb_remainder*/
  0, /*nb_divmod*/
  0, /*nb_power*/
  0, /*nb_negative*/
  0, /*nb_positive*/
  0, /*nb_absolute*/
  0, /*nb_nonzero*/
  0, /*nb_invert*/
  0, /*nb_lshift*/
  0, /*nb_rshift*/
  0, /*nb_and*/
  0, /*nb_xor*/
  0, /*nb_or*/
  0, /*nb_coerce*/
  0, /*nb_int*/
  0, /*nb_long*/
  0, /*nb_float*/
  0, /*nb_oct*/
  0, /*nb_hex*/
  0, /*nb_inplace_add*/
  0, /*nb_inplace_subtract*/
  0, /*nb_inplace_multiply*/
  0, /*nb_inplace_divide*/
  0, /*nb_inplace_remainder*/
  0, /*nb_inplace_power*/
  0, /*nb_inplace_lshift*/
  0, /*nb_inplace_rshift*/
  0, /*nb_inplace_and*/
  0, /*nb_inplace_xor*/
  0, /*nb_inplace_or*/
  0, /*nb_floor_divide*/
  0, /*nb_true_divide*/
  0, /*nb_inplace_floor_divide*/
  0, /*nb_inplace_true_divide*/
};

static PySequenceMethods __pyx_tp_as_sequence_vorbissimple = {
  0, /*sq_length*/
  0, /*sq_concat*/
  0, /*sq_repeat*/
  0, /*sq_item*/
  0, /*sq_slice*/
  0, /*sq_ass_item*/
  0, /*sq_ass_slice*/
  0, /*sq_contains*/
  0, /*sq_inplace_concat*/
  0, /*sq_inplace_repeat*/
};

static PyMappingMethods __pyx_tp_as_mapping_vorbissimple = {
  0, /*mp_length*/
  0, /*mp_subscript*/
  0, /*mp_ass_subscript*/
};

static PyBufferProcs __pyx_tp_as_buffer_vorbissimple = {
  0, /*bf_getreadbuffer*/
  0, /*bf_getwritebuffer*/
  0, /*bf_getsegcount*/
  0, /*bf_getcharbuffer*/
};

statichere PyTypeObject __pyx_type_12vorbissimple_vorbissimple = {
  PyObject_HEAD_INIT(0)
  0, /*ob_size*/
  "vorbissimple.vorbissimple", /*tp_name*/
  sizeof(struct __pyx_obj_12vorbissimple_vorbissimple), /*tp_basicsize*/
  0, /*tp_itemsize*/
  __pyx_tp_dealloc_12vorbissimple_vorbissimple, /*tp_dealloc*/
  0, /*tp_print*/
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  0, /*tp_compare*/
  0, /*tp_repr*/
  &__pyx_tp_as_number_vorbissimple, /*tp_as_number*/
  &__pyx_tp_as_sequence_vorbissimple, /*tp_as_sequence*/
  &__pyx_tp_as_mapping_vorbissimple, /*tp_as_mapping*/
  0, /*tp_hash*/
  0, /*tp_call*/
  0, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  &__pyx_tp_as_buffer_vorbissimple, /*tp_as_buffer*/
  Py_TPFLAGS_DEFAULT|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_HAVE_GC, /*tp_flags*/
  0, /*tp_doc*/
  __pyx_tp_traverse_12vorbissimple_vorbissimple, /*tp_traverse*/
  __pyx_tp_clear_12vorbissimple_vorbissimple, /*tp_clear*/
  0, /*tp_richcompare*/
  0, /*tp_weaklistoffset*/
  0, /*tp_iter*/
  0, /*tp_iternext*/
  __pyx_methods_12vorbissimple_vorbissimple, /*tp_methods*/
  0, /*tp_members*/
  0, /*tp_getset*/
  0, /*tp_base*/
  0, /*tp_dict*/
  0, /*tp_descr_get*/
  0, /*tp_descr_set*/
  0, /*tp_dictoffset*/
  0, /*tp_init*/
  0, /*tp_alloc*/
  __pyx_tp_new_12vorbissimple_vorbissimple, /*tp_new*/
  0, /*tp_free*/
  0, /*tp_is_gc*/
  0, /*tp_bases*/
  0, /*tp_mro*/
  0, /*tp_cache*/
  0, /*tp_subclasses*/
  0, /*tp_weaklist*/
};

static struct PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};

DL_EXPORT(void) initvorbissimple(void); /*proto*/
DL_EXPORT(void) initvorbissimple(void) {
  __pyx_m = Py_InitModule4("vorbissimple", __pyx_methods, 0, 0, PYTHON_API_VERSION);
  if (!__pyx_m) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 5; goto __pyx_L1;};
  __pyx_b = PyImport_AddModule("__builtin__");
  if (!__pyx_b) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 5; goto __pyx_L1;};
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 5; goto __pyx_L1;};
  if (__Pyx_InternStrings(__pyx_intern_tab) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 5; goto __pyx_L1;};
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 5; goto __pyx_L1;};
  __pyx_type_12vorbissimple_vorbissimple.tp_free = _PyObject_GC_Del;
  if (PyType_Ready(&__pyx_type_12vorbissimple_vorbissimple) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 40; goto __pyx_L1;}
  if (PyObject_SetAttrString(__pyx_m, "vorbissimple", (PyObject *)&__pyx_type_12vorbissimple_vorbissimple) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 40; goto __pyx_L1;}
  __pyx_ptype_12vorbissimple_vorbissimple = &__pyx_type_12vorbissimple_vorbissimple;

  /* "/data/home/matteh/kamaelia/head/Code/Python/Bindings/vorbissimple/python/vorbissimple.pyx":134 */
  return;
  __pyx_L1:;
  __Pyx_AddTraceback("vorbissimple");
}

static char *__pyx_filenames[] = {
  "vorbissimple.pyx",
};
statichere char **__pyx_f = __pyx_filenames;

/* Runtime support code */

static PyObject *__Pyx_GetName(PyObject *dict, PyObject *name) {
    PyObject *result;
    result = PyObject_GetAttr(dict, name);
    if (!result)
        PyErr_SetObject(PyExc_NameError, name);
    return result;
}

static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb) {
    Py_XINCREF(type);
    Py_XINCREF(value);
    Py_XINCREF(tb);
    /* First, check the traceback argument, replacing None with NULL. */
    if (tb == Py_None) {
        Py_DECREF(tb);
        tb = 0;
    }
    else if (tb != NULL && !PyTraceBack_Check(tb)) {
        PyErr_SetString(PyExc_TypeError,
            "raise: arg 3 must be a traceback or None");
        goto raise_error;
    }
    /* Next, replace a missing value with None */
    if (value == NULL) {
        value = Py_None;
        Py_INCREF(value);
    }
    /* Next, repeatedly, replace a tuple exception with its first item */
    while (PyTuple_Check(type) && PyTuple_Size(type) > 0) {
        PyObject *tmp = type;
        type = PyTuple_GET_ITEM(type, 0);
        Py_INCREF(type);
        Py_DECREF(tmp);
    }
    if (PyString_Check(type))
        ;
    else if (PyClass_Check(type))
        ; /*PyErr_NormalizeException(&type, &value, &tb);*/
    else if (PyInstance_Check(type)) {
        /* Raising an instance.  The value should be a dummy. */
        if (value != Py_None) {
            PyErr_SetString(PyExc_TypeError,
              "instance exception may not have a separate value");
            goto raise_error;
        }
        else {
            /* Normalize to raise <class>, <instance> */
            Py_DECREF(value);
            value = type;
            type = (PyObject*) ((PyInstanceObject*)type)->in_class;
            Py_INCREF(type);
        }
    }
    else {
        /* Not something you can raise.  You get an exception
           anyway, just not what you specified :-) */
        PyErr_Format(PyExc_TypeError,
                 "exceptions must be strings, classes, or "
                 "instances, not %s", type->ob_type->tp_name);
        goto raise_error;
    }
    PyErr_Restore(type, value, tb);
    return;
raise_error:
    Py_XDECREF(value);
    Py_XDECREF(type);
    Py_XDECREF(tb);
    return;
}

static int __Pyx_InternStrings(__Pyx_InternTabEntry *t) {
    while (t->p) {
        *t->p = PyString_InternFromString(t->s);
        if (!*t->p)
            return -1;
        ++t;
    }
    return 0;
}

static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        if (!*t->p)
            return -1;
        ++t;
    }
    return 0;
}

#include "compile.h"
#include "frameobject.h"
#include "traceback.h"

static void __Pyx_AddTraceback(char *funcname) {
    PyObject *py_srcfile = 0;
    PyObject *py_funcname = 0;
    PyObject *py_globals = 0;
    PyObject *empty_tuple = 0;
    PyObject *empty_string = 0;
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;
    
    py_srcfile = PyString_FromString(__pyx_filename);
    if (!py_srcfile) goto bad;
    py_funcname = PyString_FromString(funcname);
    if (!py_funcname) goto bad;
    py_globals = PyModule_GetDict(__pyx_m);
    if (!py_globals) goto bad;
    empty_tuple = PyTuple_New(0);
    if (!empty_tuple) goto bad;
    empty_string = PyString_FromString("");
    if (!empty_string) goto bad;
    py_code = PyCode_New(
        0,            /*int argcount,*/
        0,            /*int nlocals,*/
        0,            /*int stacksize,*/
        0,            /*int flags,*/
        empty_string, /*PyObject *code,*/
        empty_tuple,  /*PyObject *consts,*/
        empty_tuple,  /*PyObject *names,*/
        empty_tuple,  /*PyObject *varnames,*/
        empty_tuple,  /*PyObject *freevars,*/
        empty_tuple,  /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        __pyx_lineno,   /*int firstlineno,*/
        empty_string  /*PyObject *lnotab*/
    );
    if (!py_code) goto bad;
    py_frame = PyFrame_New(
        PyThreadState_Get(), /*PyThreadState *tstate,*/
        py_code,             /*PyCodeObject *code,*/
        py_globals,          /*PyObject *globals,*/
        0                    /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    py_frame->f_lineno = __pyx_lineno;
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_srcfile);
    Py_XDECREF(py_funcname);
    Py_XDECREF(empty_tuple);
    Py_XDECREF(empty_string);
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}
