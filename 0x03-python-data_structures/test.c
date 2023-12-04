#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int main(void)
{
    listint_t *head, *temp;
    
	int i = 0, count = 0;
        int *array;

	head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);
    print_listint(head);

        temp = head;
        if (temp == NULL)
	{
		printf("empty\n");
                return (0);
	}

        while (temp != NULL)
        {
                count++;
                temp = temp->next;
        }
	printf("count = %d\n\n", count);
        array = malloc(sizeof(int) * count);
        if (array == NULL)
                return (-1);
        temp = head;
        while (temp != NULL)
        {
                array[i] = temp->n;
		printf("array [%d] = %d\n ****** \n", i, temp->n);
                temp = temp->next;
                i++;
        }
        for (i = 0; i < (count/2); i++)
        {
		printf("i = %d\n\n********\n", i);
                if (array[i] != array[count - 1 - i])
                        return (0);
		else
			continue;
        }
        return (0);
}
