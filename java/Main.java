import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Main.minmax();
    }

    public static void minmax() {
        var console = new Scanner(System.in);
        System.out.print("Enter the count: ");
        int count = console.nextInt();
        var max = Integer.MAX_VALUE;
        var min = Integer.MIN_VALUE;
        for (var i = 0; i < count; i++) {
            System.out.print("Enter the number: ");
            var number = console.nextInt();
            if (number < min) {
                min = number;
            }
            if (number > max) {
                max = number;
            }
        }
        console.close();
    }

    public static void days(String str) {
        var console = new Scanner(System.in);
        System.out.print("Enter the number of days: ");
        int days = console.nextInt();

        int years = days / 365;
        days = days % 365;

        int months = days / 30;
        days = days % 30;

        int weeks = days / 7;
        days = days % 7;

        System.out.println(String.format("years: %d, months: %d, weeks: %d, days: %d", years, months, weeks, days));

        console.close();
    }
}