#include "lists.h"

/**
 * check_cycle - find cycles in a linked list
 * @list: the head
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *buff1, *buff2;

	buff1 = list;
	buff2 = list;
	if (buff1 != NULL)
	{
		if (buff1 == buff1->next)
			return (1);
		while (buff1->next != NULL && buff2->next != NULL)
		{
			buff1 = buff1->next;
			buff2 = (buff2->next)->next;
			if (buff1 == buff2)
				return (1);
			if (buff2 == NULL)
				return (0);
		}
	}
	return (0);
}
