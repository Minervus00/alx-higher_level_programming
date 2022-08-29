#include "lists.h"

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(lisint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
 * is_palindrome - check if the given linked list is a palindrome
 * @head: pointer to a pointer of the start of the list
 * Return: 0 if it is not a palindrome, 1 otherwise or NULL if it fails
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev, *buff;
	int n;

	if (*head == NULL)
		return (0);
	buff = *head;
	rev = NULL;
	while (buff)
	{
		n += 1;
		add_nodeint(&rev, buff->n);
		buff = buff->next;
	}
	n = n / 2;
	buff = *head;
	while (n)
	{
		if (rev->n != buff->n)
		{
			free_listint(rev);
			return (0);
		}
		rev = rev->next;
		buff = buff->next;
		n -= 1;
	}
	free_listint(rev);
	return (1);
}
