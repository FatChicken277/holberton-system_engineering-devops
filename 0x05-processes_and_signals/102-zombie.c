#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid < 1)
			return (0);
		printf("Zombie process created, PID: %d\n", pid);
	}
	return (infinite_while());
}
