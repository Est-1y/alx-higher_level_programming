#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - linked lists
 * @m: the integer
 * @next: points next node
 * Description: linked list node structures
 *
 */
typedef struct listint_s
{
	int m;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int m);
void free_listint(listint_t *head);
listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
