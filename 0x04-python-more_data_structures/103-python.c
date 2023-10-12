#include <Python.h>
void print_python_list(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    printf("[");
    for (int i = 0; i < size; i++) {
        printf(" %p", PyList_GetItem(p, i));
        if (i < size - 1) {
            printf(", ");
        }
    }
    printf(" ]\n");
}
void print_python_bytes(PyObject *p) {
    Py_ssize_t size = PyBytes_GET_SIZE(p);
    printf("b\"");
    for (int i = 0; i < size && i < 10; i++) {
        printf("%c", PyBytes_AS_STRING(p)[i]);
    }
    if (size > 10) {
        printf("...");
    }
    printf("\"\n");
}
