#include "lists.h"
/**
 *
 */
size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t copy = *h;
	dlistint_t *temp = &copy;
	int count = 0;

	while (temp != NULL)
	{
		count++;
		printf("%d\n", temp->n);
		temp = temp->next;
	}
	return (count);
}
