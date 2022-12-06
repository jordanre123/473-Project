class Flights:
    """Encapsulates an Amazon DynamoDB table of flight data."""
    def __init__(self, dyn_resource):
        """
        :param dyn_resource: A Boto3 DynamoDB resource.
        """
        self.dyn_resource = dyn_resource
        self.table = None

    def add_flight(self, success, flight_time, pilot, academic_dptmnt, checkpoints, controller, final_landing_point):
        try:
            self.table.put_item(
                Item={
                    'success': success,
                    'flight_time': flight_time,
                    'pilot': pilot,
                    'academic_dptmnt': academic_dptmnt,
                    'checkpoints': checkpoints,
                    'controller': controller,
                    'final_landing_point': final_landing_point})
        except ClientError as err:
            logger.error(
                "Couldn't add flight %s to table %s. Here's why: %s: %s",
                pilot, self.table.name,
                err.response['Error']['Code'], err.response['Error']['Message'])
            raise