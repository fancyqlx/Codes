#include <stdio.h>
#include <stdlib.h>


void get_time(int *hour, int *min, int *second, int const time_diff_second)
{
	// implement your code here
    int t_time = *hour * 3600 + *min * 60 + *second;
    int m_time = time_diff_second;
    if(m_time < 0) m_time = -((-time_diff_second)%86400);
    else m_time %= 86400;
    t_time += m_time;
    *hour = t_time/3600;
    *min = t_time/60-*hour*60;
    *hour %= 24;
    *second = t_time%60;
}

int main()
{
	int hour, min, second, time_diff_second;

    	while (scanf("%d:%d:%d,%d", &hour, &min, &second, &time_diff_second) != EOF) {
        
		get_time(&hour, &min, &second, time_diff_second);
		printf("%02d %02d %02d\n", hour, min, second);
	}
}