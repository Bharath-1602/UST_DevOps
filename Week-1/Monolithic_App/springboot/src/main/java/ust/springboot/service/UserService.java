package ust.springboot.service;

import org.springframework.stereotype.Service;
import java.util.List;
import ust.springboot.entity.User;
import ust.springboot.repository.UserRepository;

@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User createUser(User user) {
        return userRepository.save(user);
    }

    public List<User> getAllUsers() {
        return userRepository.findAll();
    }
}