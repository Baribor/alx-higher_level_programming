#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
}

void print_python_float(PyObject *p)
{
}

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t alloc, size, i;
	char *type;

	fflush(stdout);

	printf("[*] Python list info\n");

	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("   [ERROR] Invalid List Object");
		return;
	}

	alloc = list->allocated;
	size = list->ob_base.ob_size;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; ++i)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "float"))
			print_python_float(p);
		else if (strcmp(type, "byte"))
			print_python_bytes(p);
	}
}
