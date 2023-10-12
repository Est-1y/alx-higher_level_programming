#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * print_dlistint - prints dlistint elements
 * @h: list head
 * Return: nodes number
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;
	const dlistint_t *current = h;

	while (current != NULL)
	{
		printf("%d ", current->n);
		current = current->next;
		count++;
	}

	printf("\n");
	return (count);
}
