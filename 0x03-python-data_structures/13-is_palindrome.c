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
	int length, j;
	listint_t *left_head, *right_head;

	if (!head)
		return (0);

	length = len(head);

	if (length == 0)
		return (1);

	left_head = right_head = *head;
	j = length - 1;

	while (left_head)
	{
		if (left_head->n != right_head[j * 2].n)
			return (0);
		left_head = left_head->next;
		j -= 1;
	}

	return (1);
}
