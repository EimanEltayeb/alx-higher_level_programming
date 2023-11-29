#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/*
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (head == NULL)
	{
		*head = new;
		return (new);
	}
	new->n = number;
	temp = *head;
	if (temp->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (temp->next != NULL)
		{
			if (number > temp->next->n)
			{
				temp = temp->next;
				continue;
			}
			else
			{
				new->next = temp->next;
				temp->next = new;
				return (new);
			}
		}
		temp->next = new;
		new->next = NULL;
		return (new);
	}
	return (new);
}
