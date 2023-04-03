#include <Python.h>
#include <floatobject.h>

void print_python_list(PyObject *p)
{
    int i, size;
    PyObject *item;

    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid List Object\n");
        fflush(stdout);
        return;
    }

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
    }
    fflush(stdout);
}


void print_python_bytes(PyObject *p)
{
    int i, size;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid Bytes Object\n");
        fflush(stdout);
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[*] Size of the Python Bytes = %d\n", size);
    printf("[*] Bytes object content:");

    if (size > 10) {
        size = 10;
    }

    for (i = 0; i < size; i++) {
        printf(" %02x", (unsigned char)str[i]);
    }

    printf("\n");
    fflush(stdout);
}


void print_python_float(PyObject *p)
{
    char *str;
    double value;

    printf("[.] float object info\n");

    if (!PyFloat_Check(p)) {
        printf("[ERROR] Invalid Float Object\n");
        fflush(stdout);
        return;
    }

    value = PyFloat_AsDouble(p);
    str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

    printf("[*] value: %s\n", str);
    fflush(stdout);
}
