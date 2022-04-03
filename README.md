# SatNOGS Priority Schedule

#### License: AGPLv3

#### Authors: Ethan Hawk, Nick Koeppen, Erik Petersen, SatNOGS Developer Team

#

## About

This is a student-led project directed under Professor Dan White (Valparaiso University) and his ideal to revolutionize the way in which satellites are scheduled to communicate with ground stations in the SatNOGS database. It is based, in part, off of the existing SatNOGS auto-scheduler, but is also meant to implement a deeper 'bidding'-like system in which satellites and ground-stations can set priorities.

For example, a satellite owner may prefer quantity over quality, meaning they are able to have more poorer connections to their satellite as opposed to having less connections but having them more stable and uninterfered. On the other hand, a ground station owner may want to always have their ground station in use, or may only want to dedicate power and time to projects only if the reliability of the satellite is higher than a specific threshold. 

While this project is not meant to program the algorithms for such specific connection-scheduling needs, it is meant to rather provide a framework in which these plugins can be added. 

#

## How it Works

1. The satellite creates a list of ground stations and utilizes a sigmoid function, which is determined from a list of preferences given to the satellite owner, to establish its priority for each ground station. 

2. This list of ground stations, created by the satellite, is then randomized (so as to eliminate any other biases) and sent to all ground stations which are capable of communicating with the satellite in question. Each ground station uses this list to compile its own list of satellites which it can communicate with. Like the list from the satellite, this list will also use a sigmoid function in order to calculate its own preferences of each satellite. Factors that may influence the sigmoid function of the list of satellites consist of, but are not limited to, ...
a.) The predicted strengh/reliability of communication between the satellite and the ground station
b.) The country of origin of the satellite
c.) The satellite's own sigmoid result (preference) of the ground station

3. The first satellite to reach the ground station's sigmoid result threshold is then set on the schedule, and the process repeats for other times. 