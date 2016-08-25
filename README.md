## Project: Tournament Results - Alessandro Giacomini
## Description
-----------------------------------
Has been defined the database schema for a Swiss tournament system and written a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament uses the Swiss system for pairing up players in each round: players are not eliminated, and each player is paired with another player with the same number of wins, or as close as possible.

### Installation
-----------------------------------
* [Vagrant](https://www.vagrantup.com/)
* [Virtual Box](https://www.virtualbox.org/)
* Python
* [Clone the fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) in the vagrant directory of the clone
* Delete the existing tournament directory and clone this [repo](https://github.com/AlessandroGiacomini/swissSystemTournament.git)
* In the command line navigate to the vagrant directory and launch the VM

```bash
vagrant$ vagrant up
vagrant$ vagrant ssh
```

Navigate in the VM to the vagrant directory

```bash
cd /vagrant/swissSystemTournament
python tournament_test.py
```

### Citations
-----------------------------------
Udacity forums and StackOverflow forums.