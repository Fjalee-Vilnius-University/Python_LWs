#include <Python.h>

int main(int argc, char * argv[]) {
  printRandomNumber();
  return 0;
}

void printRandomNumber() {
  Py_Initialize();
  PyRun_SimpleString("import random\n"
    "n = random.random()\n"
    "print(n)\n");
  Py_Finalize();
}