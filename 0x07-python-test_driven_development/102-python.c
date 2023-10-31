#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <locale.h>
#include <Python.h>
#include <unicodeobject.h>

/**
 * print_python_sting - This prints information 
 * about python strings
 * @x: the address of pyobject struct
 */
void print_python_string(PyObject *x)
{
	wprintf(L"[.] string object info\n");
	if (strcmp(x->ob_type->tp_name, "str"))
	{
		wprintf(L"  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(s))
		wprintf(L"  type: compact ascii\n");
	else
		wprintf(L"  type: compact unicode object\n");
	wprintf(L"  length: %lu\n", PyUnicode_GET_LENGTH(x));
	wprintf(L"  value: %ls\n", PyUnicode_AS_UNICODE(x));
}
