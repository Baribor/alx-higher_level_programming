#include "lists.h"

/**
 * check_cycle - Checks if a circle exist in a linked list
 * @list: Point to the head of a list
 * Return: 0 if no circle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	hare = tortoise = list;

	while (hare && tortoise && hare->next && tortoise->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}

	return (0);
}
