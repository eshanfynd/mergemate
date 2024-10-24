public class Main {
    public static void main(String[] args) {
        int result = sumNumbers(100);
        System.out.println("Sum of numbers from 1 to 100 is: " + result);
    }

    public static int sumNumbers(int n) {
        int total = 0;
        for (int i = 1; i <= n; i++) {
            total += i;  // Adding each number to total
        }
        return total;
    }
    
}
