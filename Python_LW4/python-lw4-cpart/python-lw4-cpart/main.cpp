#include <stdio.h>
#include <Python.h>

int testFind(int num1, int num2) {
    return 19;
}

 static PyObject * testFunc(PyObject *self, PyObject *args){ 
    //  const char *command;
    int sts, num1, num2;
    if (!PyArg_ParseTuple(args, "il", &num1, &num2)) 
       return NULL;
    sts = testFind(num1, num2);
    return PyLong_FromLong(sts);
    // sts = system(command);
    // if (sts < 0) { 
    //    //PyErr_SetString(spamError,&"System&command&failed");&
    //    return NULL; 
    // } 
     //return Py_BuildValue("i", sts); 
 }

 static PyObject* version(PyObject* self) {
     return Py_BuildValue("s", "Version 0.01");
 }

 static PyMethodDef Examples[] = {
     {"testFunc", testFunc, METH_VARARGS, "testString"},
     {"version", (PyCFunction)version, METH_NOARGS, "returns the version"},
     {NULL, NULL, 0, NULL}
 };

 static struct PyModuleDef Example = {
    PyModuleDef_HEAD_INIT,
    "Example",
    "test Module",
    -1,
    Examples
 };

 PyMODINIT_FUNC PyInit_Example(void){
     return PyModule_Create(&Example);
 }