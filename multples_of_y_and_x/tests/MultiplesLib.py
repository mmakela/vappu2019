from robot.libraries import OperatingSystem


class MultiplesError(Exception):
    pass


class MultiplesLib(OperatingSystem.OperatingSystem):

    def __init__(self, infile, outfile):
        self._infile = infile
        self._outfile = outfile

    def _run_script(self):
        return self.run_and_return_rc_and_output(
            'python multples_of_y_and_x.py {} {}'.format(
                self._infile, self._outfile))

    def run_successful_script(self):
        rc, output = self._run_script()
        if rc != 0:
            raise MultiplesError('Unexpected rc={}'.format(rc))
        return output

    def run_unsuccessful_script(self):
        rc, output = self._run_script()
        if rc > 0:
            return output
        raise MultiplesError('Expected script to fail, instead got rc={}'.format(rc))
