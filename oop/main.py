from class_static_methods_demo import Calculator

def main():
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    print("Calculation type:", Calculator.get_calculation_type())

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
