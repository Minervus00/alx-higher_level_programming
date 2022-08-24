#include "lists.h"

/**
 * check_cycle - find cycles in a linked list
 * @list: the head
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *buff, *h;

	buff = list;
	h = NULL;
	if (buff != NULL)
	{
		h = buff->next;
		while (h != NULL)
		{
			while (buff != h)
			{
				if (h->next == buff)
					return (1);
				buff = buff->next;
			}
			buff = list;
			h = h->next;
		}
	}
	return (0);
}
