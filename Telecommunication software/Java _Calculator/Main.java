import java.util.Scanner;

class Main {
    public static void main(String[] args) {

        char SimpleCalculator;
        Double Fnum, Snum, Result;
        Boolean test;

        Scanner Xx_xX = new Scanner(System.in);

        System.out.println("Choose the first number");        // ask users to enter the first number of the operation
        Fnum = Xx_xX.nextDouble();

        test=false;
        System.out.println("Choose the operation you want to proceed : +, -, *, or /");        // ask users to choose the operation for the two numbers
        SimpleCalculator = Xx_xX.next().charAt(0);
        while (test == false) {
            switch (SimpleCalculator){
                case '+':
                    test=true;
                    break;
                case '-':
                    test=true;
                    break;
                case '*':
                    test=true;
                    break;
                case '/':
                    test=true;
                    break;
                default:
                    System.out.println("Invalid operator! You have to choose between +, -, *, and /");
                    System.out.println("Choose the operation you want to proceed : +, -, *, or /");        // ask users to choose the operation for the two numbers
                    SimpleCalculator = Xx_xX.next().charAt(0);
                    break;
            }
        }
        System.out.println("Choose the second number");        // ask users to enter the second number of the operation
        Snum = Xx_xX.nextDouble();

        switch (SimpleCalculator) {

            case '+':
                Result = Fnum + Snum;
                System.out.println(Fnum + " + " + Snum + " = " + Result);
                break;

            case '-':
                Result = Fnum - Snum;
                System.out.println(Fnum + " - " + Snum + " = " + Result);
                break;

            case '*':
                Result = Fnum * Snum;
                System.out.println(Fnum + " * " + Snum + " = " + Result);
                break;

            case '/':
                Result = Fnum / Snum;
                System.out.println(Fnum + " / " + Snum + " = " + Result);
                break;

            default: // other cases than the 4 basic operations (normally not possible)
                System.out.println("??????");
                break;
        }

        Xx_xX.close();
    }
}