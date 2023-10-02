#include "lists.h"

/**
 * check_cycle - checks a cycle in linked lists
 * @list: list to be checked
 * Return: 1 (list has a cycle), 0 (no cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
