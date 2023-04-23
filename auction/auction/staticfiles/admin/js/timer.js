const intervalId = setInterval(function() {
    item.timeRemaining -= 1000;
    if (item.timeRemaining <= 0) {
      clearInterval(intervalId);
      timer.textContent = '00:00:00';
      listItem.style.backgroundColor = '#f8d7da';
    } else {
      const hours = Math.floor(item.timeRemaining / (60 * 60 * 1000));
      const minutes = Math.floor((item.timeRemaining % (60 * 60 * 1000)) / (60 * 1000));
      const seconds = Math.floor((item.timeRemaining % (60 * 1000)) / 1000);

      const formattedHours = hours.toString().padStart(2, '0');
      const formattedMinutes = minutes.toString().padStart(2, '0');
      const formattedSeconds = seconds.toString().padStart(2, '0');

      timer.textContent = `${formattedHours}:${formattedMinutes}:${formattedSeconds}`;
    }
  }, 1000);