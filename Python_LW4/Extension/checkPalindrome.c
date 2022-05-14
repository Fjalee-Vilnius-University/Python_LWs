#include <Python.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>

static PyObject *errStr;

static PyObject * fibonacci_nth_nm(PyObject *self, PyObject *args)
{
  char *str = NULL;
  int len = 0;
  int temp = 0;

  if (!PyArg_ParseTuple(args, "s", &str))
  {
    return NULL;
  }

  len = strlen(str);
  if(len == 0)
  {
    PyErr_Format(errStr, "Can't handle empty string");
  }

  for(int i = 0; i < len; i++)
  {
    if (str[i] != str[len - i - 1])
    {
      temp = 1;
      break;
    }
  }

  return PyLong_FromLong(temp);
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
  errStr = PyErr_NewException("errStr.error", NULL, NULL);
  Py_INCREF(errStr);
  PyModule_AddObject(module, "error", errStr);
}
