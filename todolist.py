class ToDoList:
    def __init__(self):
        self.tasks=[]
    def add_task(self,task):
        self.tasks.append(task)
    def delete_task(self,task_index):
        if 0<=task_index<len(self.tasks):
            del self.tasks[task_index]
        else:
            print("invalid task index")
    def mark_completed(self,task_index):
        if 0<=task_index<len(self.tasks):
            task=self.tasks(task_index)
            print(f"Task{task_index+1}:{task} is marked as completed")
        else:
            print("Invalid task index")
    def display_tasks(self):
        for i,task in enumerate(self.tasks):
            print(f"task{i+1};{task}")
def main():
    to_do_list=ToDoList()
    while True:
        print("\n To Do List Applictaion")
        print("1.Add Task")
        print("2.Delete Task")
        print("3.Mark As Completed")
        print("4.Display Tasks")
        print("5.Quit")
        option=int(input("enter your option:"))
        if option==1:
            task=input("Enter the task:")
            to_do_list.add_task(task)
        elif option==2:
            task_index=int(input("enter the task index to delete:"))-1
            to_do_list.delete_task(task_index)
        elif option==3:
            task_index=int(input("enter the task index to mark as completed:"))
        elif option==4:
            to_do_list.display_tasks()
        elif option==5:
            break
        else:
            print("Invalid option Please Try Again!!")

if __name__=="__main__":
    main()