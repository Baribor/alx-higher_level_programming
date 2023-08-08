#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Adds a node to a sorted linked list
 * @head: Pointer to the head of the list
 * @number: Value of the new list
 * Return: Pointer to the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node, *prev_node = NULL;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	if (!*head)
	{
		*head = new_node;
		return (new_node);
	}
	current_node = *head;

	while (current_node)
	{
		if (current_node->n >= new_node->n)
		{
			new_node->next = current_node;
			if (!prev_node)
				*head = new_node;
			else
				prev_node->next = new_node;
			return (new_node);
		}

		prev_node = current_node;
		current_node = current_node->next;
	}

	prev_node->next = new_node;
	return (new_node);
}
