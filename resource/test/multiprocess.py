import multiprocessing

square_result = []
def calc_square(numbers):
    global square_result
    for n in numbers:
        print('Square : ', str(n*n))
        square_result.append(n*n)
    print('Result : ', str(square_result))

if __name__ == '__main__':
    arr = [2, 3, 4, 5]

    p1 = multiprocessing.Process(target=calc_square, args=(arr, ))
    p1.start()
    p1.join()

    print('Result : ', str(square_result))
    print('Done!')
