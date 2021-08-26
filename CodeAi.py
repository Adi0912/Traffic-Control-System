#include<stdio.h>
#include<fcntl.h>
#include<string.h>
#include<stdlib.h>
#include<pthread.h>
void main()
{
    int i,j,pt[10],wait_t[10],totalwait_t=0,pr[10],tp1,n;          //pt= process time, wait_t=waiting time, pr=priority
    char p[10][5],tp[5];
    float avgwait_t;
    printf("This is leve1, Preemptive(Priority Scheduling)\n");
    printf("Enter the number of processes:");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("Enter the process %d name: ",i+1);
        scanf("%s",&p[i]);
        printf("Enter the process time: ");
        scanf("%d",&pt[i]);
        printf("Enter the priority: ");
        scanf("%d",&pr[i]);
    }
    for(i=0;i<n-1;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(pr[i]>pr[j])
            {
                tp1=pr[i];
                pr[i]=pr[j];
                pr[j]=tp1;
                tp1=pt[i];
                pt[i]=pt[j];
                pt[j]=tp1;
                strcpy(tp,p[i]);
                strcpy(p[i],p[j]);
                strcpy(p[j],tp);
            }
        }
    }
    wait_t[0]=0;
    for(i=1;i<n;i++)
    {
        wait_t[i]=wait_t[i-1]+wait_t[i-1];
        totalwait_t=totalwait_t+wait_t[i];
    }
    avgwait_t = totalwait_t/n;
    printf("Process name \t Processing time \t priority\t Waiting time\n");
    for(i=0;i<n;i++)
    {
       printf(" %s      \t \t %d \t     \t %d \t   \t %d \n" ,p[i],pt[i],pr[i],wait_t[i]);
    }
    printf("Total Waiting Time = %d \n",&totalwait_t);
    printf("Average Waiting time = %f \n",&avgwait_t);
    printf("\n\nThank You for reading the code snippet by Aditya\n\n");
   
    int ts,pid[10],nd[10],wait_t1[10],tat[10],i1,j1,n2,n1;
    int bt[10],flag[10],totat=0,tot_wait_t=0;
    float avgwait_t2,avgtat;
    printf("This is the level 2, Round Robin Scheduling");
    printf("\n Enter the number of Processes \n");
    scanf("%d",&n);
    n1=n;
    printf("\n Enter the Timeslice(Quanta must be multiple of 2): ");
    scanf("%d",&ts);
    for(i=1;i<=n;i++)
    {
        printf("\n Enter the process ID for %d:  ",i);
        scanf("%d",&pid[i]);
        printf("\n Enter the Burst Time for the process:  ");
        scanf("%d",&bt[i]);
        nd[i]=bt[i];
    }
    for(i=1;i<=n;i++)
    {
        flag[i]=1;
        wait_t[i]=0;
    }
    while(n!=0)
    {
        for(i=1;i<=n;i++)
        {
            if(nd[i]>=ts)
            {
                for(j=1;j<=n;j++)
                {
                    if((i!=j)&&(flag[i]==1)&&(nd[j]!=0))
                    wait_t[j]+=ts;
                }
                nd[i]= nd[i]-ts;
                if(nd[i]==0)
                {
                    flag[i]=0;
                    n--;
                }
            }
            else
            {
                for(j=1;j<=n;j++)
                {
                    if((i!=j)&&(flag[i]==1)&&(nd[j]!=0))
                    wait_t[j]+=nd[i];
                }
                nd[i]=0;
                n--;
                flag[i]=0;
            }
        }
    }
    for(i=1;i<=n1;i++)
    {
        tat[i]=wait_t[i]+bt[i];
        tot_wait_t=tot_wait_t+wait_t[i];
        totat=totat+tat[i];
    }
    avgwait_t2=(float)tot_wait_t/n1;
    avgtat=(float)totat/n1;
    printf("\n\n Process \t Process ID  \t BurstTime \t Waiting Time \t TurnaroundTime \n ");
    for(i=1;i<=n1;i++)
    {
      printf("\n %5d\t \t %5d \t\t %5d \t\t %5d \t\t %5d \n", i,pid[i],bt[i],wait_t[i],tat[i]);
    }
    printf("\n The average Waiting Time= %2f",avgwait_t2);
    printf("\n The average Turn around Time= %2f ",avgtat);
    printf("\n\nThank You for reading the code snippet by Aditya\n\n");
}
