#include "lists.h"
/**
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1;
	listint_t *temp2;

	temp1 = list;
	temp2 = list->next;
	if (list == NULL)
		return (0);

	while (temp1 != NULL && temp2->next != NULL)
	{
		if (temp1 == temp2)
			return (1);
		else
		{
			temp1 = temp1->next;
			temp2 = temp2->next->next;
		}
	}
	return (0);
}
