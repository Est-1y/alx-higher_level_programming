#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - linked list
 * @q: the integer
 * @next: points next node
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int q;
	struct listint_s *next;
} listint_t;

void free_listint(listint_t *head);
int check_cycle(listint_t *list);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int q);

#endif /* LISTS_H */
