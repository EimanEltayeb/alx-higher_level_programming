#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 *
 */
int is_palindrome(listint_t **head)
{
	int i = 0, count = 0;
	int *array;

	listint_t *temp;
	temp = *head;
	if (temp == NULL)
		return (1);

	while (temp != NULL)
	{
		count++;
		temp = temp->next;
	}
	array = malloc(sizeof(int) * count);
	if (array == NULL)
		return (-1);
	temp = *head;
	while (temp != NULL)
	{
		array[i] = temp->n;
		temp = temp->next;
		i++;
	}
	for (i = 0; i < (count / 2); i++)
	{
		if (array[i] != array[count - 1 - i])
			return (0);
		else
			continue;
	}
	return (1);
}
