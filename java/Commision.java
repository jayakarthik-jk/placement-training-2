import java.util.Scanner;

public class Commision {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);

        System.out.print("Enter the salary: ");
        int salary = console.nextInt();
        System.out.print("Enter the sales: ");
        int sales = console.nextInt();

        int percent = 0;
        if (sales < 5000) {
            percent = 0;
        } else if (sales < 10000) {
            percent = 5;
        } else if (sales < 20000) {
            percent = 10;
        } else if (sales < 30000) {
            percent = 12;
        } else {
            percent = 15;
        }

        int commision = salary / 100 * percent;
        System.out.println("The commision is " + commision);
        System.out.println("The final salary is " + (salary + commision));

        console.close();
    }
}
