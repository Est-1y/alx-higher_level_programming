#include "lists.h"

#include "lists.h"

/**
 * print_dlistint - prints dlistint elements
 * @h: list head
 * Return: nodes number
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);

		h = h->next;
		count++;
	}

	return (count);
}
