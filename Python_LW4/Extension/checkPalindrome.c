#include <Python.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>

static PyObject *moduleError;

static PyObject * fibonacci_nth_nm(PyObject *self, PyObject *args)
{
  int n = 0;

  if (!PyArg_ParseTuple(args, "i", &n))
  {
    PyErr_Format(moduleError, "Can't parse input");
    return NULL;
  }

  if(n < 0)
  {
    PyErr_Format(moduleError, "Can't handle negative numbers");
    return NULL;
  }

  return PyLong_FromLong(n);
}

static PyMethodDef fibonacciModuleMethods[] = {
  {"fibonacci_nth_nm", fibonacci_nth_nm, METH_VARARGS, "module for finding fibonacci nth number"},
  {NULL, NULL, 0, NULL}
};


static struct PyModuleDef fibonacciNthNmModule = {
  PyModuleDef_HEAD_INIT,
  "getFibonacciNthNm",
  "function for finding fibonacci nth number",
  -1,
  fibonacciModuleMethods
};

PyMODINIT_FUNC PyInit_checkPalindrome(void)
{
  return PyModule_Create(&fibonacciNthNmModule);
}

PyMODINIT_FUNC PyInit_empty(void)
{
  PyObject * module = PyModule_Create( &fibonacciNthNmModule);
  moduleError = PyErr_NewException("module.error", NULL, NULL);
  Py_INCREF(moduleError);
  PyModule_AddObject(module, "error", moduleError);
}
