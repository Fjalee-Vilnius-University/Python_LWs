#include <Python.h>

#include<stdio.h>

#include<conio.h>

#include<string.h>

static PyObject *emptyStringError;


static PyObject * method_checkPalindrome(PyObject * self, PyObject * args) {
  char * str = NULL;
  int temp = 0;
  int len = 0;

  /* Parse arguments */
  if (!PyArg_ParseTuple(args,"s", & str)) {
    return NULL;
  }

  len = strlen(str);
  if(len == 0){
    PyErr_Format(emptyStringError,"Found empty string!");
  }
  for(int i = 0; i < len; i++) {
    if (str[i] != str[len - i - 1]) {
      temp = 1;
      break;
    }
  }

  return PyLong_FromLong(temp);
}

static PyMethodDef checkPalindromeMethods[] = {
    {"check_for_palindrome", method_checkPalindrome, METH_VARARGS, "Python interface for checkPalindrome function"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef checkPalindromeModule = {
    PyModuleDef_HEAD_INIT,
    "checkPalindrome",
    "Python interface for checkPalindrome function",
    -1,
    checkPalindromeMethods
};

PyMODINIT_FUNC PyInit_checkPalindrome(void) {
    return PyModule_Create(&checkPalindromeModule);
}

PyMODINIT_FUNC PyInit_empty(void) {
  PyObject * m = PyModule_Create( &checkPalindromeModule);
  emptyStringError = PyErr_NewException("emptyString.error", NULL,
    NULL);
  Py_INCREF(emptyStringError);
  PyModule_AddObject(m, "error", emptyStringError);
}