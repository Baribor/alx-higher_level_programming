#include <stdlib.h>
#include "lists.h"

/**
 * len - Gets the length of a singly linked list
 * @head: Head of the list
 * Return: Length of the list
 */
int len(listint_t **head)
{
	listint_t *h = *head;
	int length = 0;

	while (h)
	{
		length++;
		h = h->next;
	}
	return (length);
}

/**
 * is_palindrome - Checks if a singly linked list is
 * a palindrome
 * @head: Head of the list
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	int length;
	listint_t *new_head;
	int *arr, i = 0;

	if (!head)
		return (0);

	length = len(head);

	if (length == 0)
		return (1);

	arr = malloc(sizeof(int) * length);
	if (!arr)
		exit(1);

	new_head = *head;
	while (new_head)
	{
		arr[i++] = new_head->n;
		new_head = new_head->next;
	}

	new_head = *head;

	while (new_head)
	{
		if (arr[--i] != new_head->n)
		{
			free(arr);
			return (0);
		}
		new_head = new_head->next;
	}
	free(arr);
	return (1);
}
