package ust.springboot.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import ust.springboot.entity.User;

public interface UserRepository extends JpaRepository<User, Long> {
}