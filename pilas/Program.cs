using System;
using System.Collections;

namespace StackExample
{
    class Program
    {
        static void Main(string[] args)
        {
            // Crear una nueva pila
            Stack miPila = new Stack();

            // Agregar elementos a la pila
            miPila.Push("Elemento 1");
            miPila.Push("Elemento 2");
            miPila.Push("Elemento 3");
            miPila.Push("Elemento 4");
            miPila.Push("Elemento 5");

            // Mostrar los elementos en la pila
            Console.WriteLine("Elementos en la pila:");
            foreach (var item in miPila)
            {
                Console.WriteLine(item);
            }

            // Obtener y eliminar el elemento en la cima de la pila
            Console.WriteLine("\nQuitando un elemento de la pila:");
            object topItem = miPila.Pop();
            Console.WriteLine("Se ha quitado de la pila: " + topItem);

            // Mostrar los elementos restantes en la pila
            Console.WriteLine("\nElementos en la pila después de la eliminación:");
            foreach (var item in miPila)
            {
                Console.WriteLine(item);
            }

            // Verificar el elemento en la cima de la pila sin eliminarlo
            Console.WriteLine("\nElemento en la cima de la pila actualmente: " + miPila.Peek());

            // Verificar si la pila contiene un elemento específico
            Console.WriteLine("\n¿La pila contiene 'Elemento 3'? " + miPila.Contains("Elemento 3"));

            // Limpiar la pila
            miPila.Clear();
            Console.WriteLine("\nSe ha limpiado la pila. Total de elementos en la pila: " + miPila.Count);

            Console.ReadLine();
        }
    }
}
