#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the node to insert
 * @number: integer to be included in new node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev;
	listint_t *current;
	current = *head;
	/* allocate memory to store new node */
	new = malloc(sizeof(listint_t));

	if (new == NULL) /* if malloc fails */
	{
		return (NULL);
	}
	new->n = number; /* store number */
	new->next = NULL; /* new node points to nothing */
	while (current->next != NULL) /* loop through linked list */
	{
		if (new->n > current->n)
		{
			prev = current; /* store node as previous */
		}
		else
		{
			break; /* reaches where it is to be inserted */
		}
		current = current->next;
	}
	prev->next = new; /* previous node now points to new */
		new->next = current; /* new node now points to current */
		return (new);
}
