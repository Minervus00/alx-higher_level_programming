#include <Python.h>

/**
 * print_python_list_info - prints python list info
 * @p: pythonlist
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int i, n = PyList_Size(p); /*eq: len(q)*/
	int alloc = ((PyListObject *)p)->allocated; /*eq: Py_Size(p) - size allocated*/
	PyObject *itm;

	printf("[*] Size of the Python List = %d\n", n);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < n; i++)
	{
		itm = PyList_GetItem(p, i);
		/*Py_Type(itm)->tp_name = (((PyObject*)itm)->ob_type)->tp_name*/
		printf("Element %i: %s\n", i, (((PyObject*)itm)->ob_type)->tp_name);
	}
}
