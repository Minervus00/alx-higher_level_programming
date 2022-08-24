#include "lists.h"

/**
 * insert_node - insert by sorting
 * @head: the list head
 * @number: the node num
 *
 * Return: the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *buff, *node, *prev;

	node = *head;
	prev = NULL;
	while (node != NULL)
	{
		if (number <= (node->n))
			break;
		prev = node;
		node = node->next;
	}
	buff = malloc(sizeof(listint_t));
	if (buff == NULL)
		return (NULL);
	buff->n = number;
	buff->next = node;

	if (prev != NULL)
		prev->next = buff;
	else
		*head = buff;
	return (buff);
}
