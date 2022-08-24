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
	while (buff != NULL)
	{
		h = buff->next;
		while (h != NULL)
		{
			if (h->next == NULL)
				return (1);
			h = h->next;
		}
		buff = buff->next;
	}
	return (0);
}
