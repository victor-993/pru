import os
import argparse
#from resampling.modulos.algo import *

def main():
    cwd = os.getcwd()
    
    parser = argparse.ArgumentParser(description="Resampling script")

    parser.add_argument("-C", "--country", help="Country name", required=True)
    parser.add_argument("-p", "--path", help="Path to data directory", default=os.getcwd())
    parser.add_argument("-m", "--prev-months", type=int, help="Previous months", default=1)
    parser.add_argument("-c", "--cores", type=int, help="Number of cores", required=True)
    parser.add_argument("-y", "--forecast-year", type=int, help="Forecast year", required=True)

    args = parser.parse_args()

    print("Reading inputs")
    print(args)

    #print( funcion(args.country, args.path, args.prev_months, args.cores, args.forecast_year))

    # country = args.country
    # path = args.path
    # months_previous = args.prev_months
    # cores = args.coresgit
    # forecast_year = args.forecast_year

if __name__ == "__main__":
    main()