from math import sin, cos, log, exp

class Function:
    """
    A class representing a mathematical function of five variables (x1, x2, x3, x4, x5).
    """

    def __init__(self, formula: str):
        """
        Initialize the Function with a given formula. Supported math operators: sin, cos, log, exp

        Parameters
        ----------
        formula : str
            Python expression that defines the function f(x1, x2, x3, x4, x5).
            Example: "sin(x1)*cos(x2) + log(x3 + 1) + sin(x4)*sin(x5)"

        Examples
        --------
        >>> f = Function("sin(x1)*cos(x2) + log(x3 + 1) + sin(x4)*sin(x5)")
        >>> f([1, 2, 3, 4, 5])
        1.7618351566222843
        """
        self.formula = formula.strip()
        exec('self.f = lambda x1, x2, x3, x4, x5: ' + self.formula)

    def __call__(self, params: list):
        """
        Evaluate the function at the given parameters.

        Parameters
        ----------
        params : list
            A list of exactly five numerical values [x1, x2, x3, x4, x5].

        Returns
        -------
        float
            The value of the function evaluated at the given parameters.

        Raises
        ------
        ValueError
            If the number of parameters is not exactly five.
        """
        if len(params) != 5:
            raise ValueError('The number of arguments to the function must be exactly 5.')
        x1, x2, x3, x4, x5 = params
        return self.f(x1, x2, x3, x4, x5)

    def __str__(self):
        return f'f(x1, x2, x3, x4, x5) = {self.formula}'