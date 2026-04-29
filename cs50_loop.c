   #include <stdio.h>

int main(void)
{
    int count;
    {
    printf("How many times should I say hello? ");
    }
    scanf("%d", &count);

    for (int i = 0; i < count; i++)
    {
        printf("%d: Hello from Monrovia!\n", i + 1);
    }

    return 0;
}